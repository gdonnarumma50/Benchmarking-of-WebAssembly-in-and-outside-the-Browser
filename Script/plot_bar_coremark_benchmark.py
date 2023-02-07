import matplotlib.pyplot as plt

# Dati dei runtime
runtime_data = [("WasmEdge (JIT)", 14.135, 94),
                ("WasmEdge (AOT)", 19.841, 12966),
                ("Wasm3", 18.063, 11810),
                ("Wasmer", 15.702, 783)]

# Colori per i runtime
colors = ['red', 'orange', 'green', 'blue']

# Creazione del grafico a barre
fig, ax = plt.subplots()
bar_plots = []
for i, runtime in enumerate(runtime_data):
    bar_plots.append(ax.bar([i], runtime[1], color=colors[i], width=0.6))

# Aggiunta dei valori di Iteration/Sec come etichette sulle barre
for i, runtime in enumerate(runtime_data):
    ax.text(i-0.2, runtime[1]+0.1, str(runtime[2]), fontsize=8)

# Etichettatura dell'asse y
ax.set_ylabel("Tempo totale (s)")

# Titolo del grafico
plt.title("Benchmark di CoreMark 1.0")

# Assegnazione dei label ai tick delle ascisse
ax.set_xticks([i for i in range(len(runtime_data))])
ax.set_xticklabels([x[0] for x in runtime_data])

# Aggiunta di una legenda
ax.legend(bar_plots, [x[0] for x in runtime_data], loc='upper left')

# Mostra il grafico
plt.show()