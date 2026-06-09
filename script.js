const analyzeBtn = document.getElementById("analyzeBtn");

analyzeBtn.addEventListener("click", async function () {

    const code = document.getElementById("codeInput").value;
const language =
    document.getElementById("languageSelect").value;
    document.getElementById("resultBox").innerHTML =
        "<p>Analyzing code...</p>";

    try {

        const response = await fetch("http://127.0.0.1:5000/analyze", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
    code: code,
    language: language
})
        });

        const data = await response.json();

        let formattedResult = data.result
            .replace(/```python/g, "<pre><code>")
            .replace(/```/g, "</code></pre>")
            .replace(/\n/g, "<br>");

        document.getElementById("resultBox").innerHTML =
            formattedResult;

    } catch (error) {

        console.log(error);

        document.getElementById("resultBox").innerHTML =
            "Something went wrong.";

    }

});