async function buscar() {
  const trecho = document.getElementById("trecho").value.trim();
  const resultadosDiv = document.getElementById("resultados");
  resultadosDiv.innerHTML = "🔎 Buscando...";

  const resposta = await fetch("/buscar", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ trecho: trecho })
  });

  const dados = await resposta.json();

  if (dados.length === 0) {
    resultadosDiv.innerHTML = "❌ Nenhuma música encontrada.";
    return;
  }

  //PARA COLOCAR EM NEGRITO O TRECHO ENCONTRADO VAI TER QUE MEXER AQUI
  resultadosDiv.innerHTML = "";
  dados.forEach(item => {
    const bloco = document.createElement("div");
    bloco.innerHTML = `<h3>🎤 ${item.musica}</h3>`;
    item.trechos.forEach(trecho => {
      const p = document.createElement("p");
      p.textContent = `➜ ${trecho}`;
      bloco.appendChild(p);
    });
    resultadosDiv.appendChild(bloco);
  });
}
