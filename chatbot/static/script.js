function sendMessage() {
    const input = document.getElementById("msg");
    const message = input.value.trim();
    if (!message) return;

    const chatBox = document.getElementById("chat-box");

    const userDiv = document.createElement("div");
    userDiv.className = "user-msg";
    userDiv.innerText = message;
    chatBox.appendChild(userDiv);

    input.value = "";

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: message })
    })
    .then(res => res.json())
    .then(data => {
        console.log(data); // DEBUG

        const botDiv = document.createElement("div");
        botDiv.className = "bot-msg";
        botDiv.innerText = data.reply;
        chatBox.appendChild(botDiv);

        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(err => {
        alert("Frontend error");
        console.error(err);
    });
}
