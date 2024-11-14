    // Función para alternar la visibilidad del chat
    function toggleChat() {
        const chatBox = document.getElementById("chat-box");
        chatBox.classList.toggle("open");
    }
    
    function sendMessage(event) {
        if (event.key === "Enter") {
            const input = document.getElementById("user-input");
            const message = input.value;

            const messagesDiv = document.getElementById("messages");
            const userMessage = `<div><strong>Tú:</strong> ${message}</div>`;
            messagesDiv.innerHTML += userMessage;

            input.value = "";

            
            fetch('http://localhost:5005/webhooks/rest/webhook', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ sender: 'user', message: message }),
            })
            .then(response => response.json())
            .then(data => {
                // Muestra la respuesta del chatbot en la interfaz
                if (data.length > 0) {
                    const botMessage = `<div><strong>Bot:</strong> ${data[0].text}</div>`;
                    messagesDiv.innerHTML += botMessage;
                    messagesDiv.scrollTop = messagesDiv.scrollHeight;
                }
            })
            .catch(error => console.error('Error:', error));
        }
    }