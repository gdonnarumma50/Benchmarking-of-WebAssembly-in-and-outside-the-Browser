
# Benchmarking of WebAssembly in and outside the Browser

Il progetto consiste nella realizzazione di alcuni Benchmarking della tecnologia WebAssembly. I Benchmarking sono stati effettuati sia per testare la tecnologia WebAssembly su i Web Browser più conosciuto e sia per testare WebAssembly al di fuori del Browser attraverso i runtime più noti.
## Obiettivi

Gli obiettivi di questo progetto sono:
* sperimentare la tecnologia WebAssembly sul Web e al di fuori;
* testare le performance di WebAssembly sui vari Browser;
* realizzare dei micro-benchmark per valutare le performance dei runtime WebAssembly più noti.
## Configurazioni
Abbiamo testati i seguenti Browser Web:
* **Chrome**: versione 108.0.5359.124;
* **Safari**: versione 15.4;
* **Firefox**: versione 108.0.1.

L'hardware utilizzato un **MacBook Air (M1, 2020)** con le seguenti configurazioni:
* Chip: Apple M1;
* Numero totale di Core: 8 (prestazioni 4 ed efficienza 4);
* RAM: 16 GB;
* Sistema Operativo: macOS Monterey versione 12.3.

I runtime testati sono:
* [**WasmEdge**](https://github.com/WasmEdge/WasmEdge) versione 0.11.2;
* [**Wasm3**](https://github.com/wasm3/wasm3) versione 0.5.0;
* [**Wasmer**](https://github.com/wasmerio/wasmer) versione 3.1.0.

Per testare i vari Browser abbiamo utilizzato il Benchmark noto [**PSPDFKit Wasm Benchmark**](https://pspdfkit.com/webassembly-benchmark/). PSPDFKit è un kit per fornire il modo migliore di visualizzare, annotare e compilare moduli nei documenti PDF in qualsiasi piattaforma.

Per testare i vari runtime abbiamo utilizzato il tool [**Hyperfine**](https://github.com/sharkdp/hyperfine) (versione 1.15.0.), uno strumento di benchmarking a riga di comando, che consente di misurare il tempo di esecuzione di comandi o programmi sulla propria macchina.


## Workload

### Fibonacci
* Workload: calcolo della sequenza di Fibonacci ricorsiva.
* Input: 20, 30 e 40.
* Descrizione: per ogni input, la funzione di Fibonacci ricorsiva è stata eseguita per calcolare i primi 20, 30 o 40 numeri della sequenza di Fibonacci.
* Run: 100 esecuzioni per ogni runtime.

### CoreMark 1.0
Il workload è costituito da un insieme di funzioni di test, che includono:
* operazioni aritmetiche su numeri interi e floating point;
* copia e gestione delle stringhe;
* manipolazione dei bit e operazioni di confronto;
* funzioni di hashing e compressione.

Sono state effettuate 10 esecuzioni per ogni runtime.
## Implementazione
Per riprodurre i Benchmarking di WebAssembly sul Web, è sufficiente aprire la seguente pagina Web sul Browser da testare: [**PSPDFKit Wasm Benchmark**](https://pspdfkit.com/webassembly-benchmark/).

Per riprodurre i Benchmarking dei runtime WebAssembly è necessario installare WasmEdge, Wasm3 e Wasmer (controllando la versione) e installare il tool Hyperfine sulla propria macchina.

È possibile utilizzare i dataset "recursive_fibonacci.wasm" (nella directory "Fibonacci") e "coremark.wasm" (nella directory "CoreMark") per riprodurre i Benchmarking della funzione di Fibonacci ricorsiva e CoreMark 1.0.

Per riprodurre i grafici dei risultati è necessario installare **Python** con le librerie *numpy*, *matplotlib* e *scipy*. Gli script sono presenti nella cartella "Script".
Esempio esecuzione di uno script:
```shell
python plot_whisker.py fibonacci20_results.json
```

### Esempio Benchmarking
Ecco il codice di esempio per testare la funzione di Fibonacci ricorsiva con input 20.

```shell
hyperfine
-- prepare " purge "
-- export - json fibonacci20_results.json
-- runs 100
’wasmedge -- reactor recursive_fib_aot.wasm recursive_fib 20’
’wasmedge -- reactor recursive_fib.wasm recursive_fib 20’
’wasmer run recursive_fib.wasm -i recursive_fib 20’
’wasm3 -- func recursive_fib recursive_fib.wasm 20’
-i
```
## Altro
Per visualizzare i risultati e altre informazioni relative ai Benchmarking, è possibile leggere la relazione [a relative link](Benchmarkingof_WebAssembly_in_and _outside_the_Browser.pdf).
