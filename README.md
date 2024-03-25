### _ptbr_

Este projeto usa uma série de modelos de machine learning para, a partir de um vídeo em português criar uma nova versão do mesmo vídeo, mas com uma dublagem (ainda um tanto rudimentar) em inglês.

Este projeto foi criado usando `Python Poetry`. Para executar o projeto, depois de cloná-lo do Github, basta acessar o diretório do projeto e executar em seu terminal:
```bash
poetry install
poetry env use
```

Em seguida é necessário organizar um pouco os dados. Para executar o projeto corretamente é necessário colocar um arquivo `.mp4` na pasta `data/raw`. É **IMPORTANTE** que o arquivo esteja nomeado `case_ai.mp4`.

Feito isso basta executar  o arquivo `main.py`.

Foram tomados cuidados para usar modelos de machine learning _open source_ na maior parte das feses do projeto. Alguns desses modelos merecem algumas considerações.

[TRANSCRIÇÃO] `openai-whisper` Além de trazer uma boa qualidade o modelo entrega nos seus resultados diversos outputs úteis, como arquivos que podem ser usados diretamente para criar legendas bem como uma minutagem muito eficiente.

[TRADUÇÃO] Os resultados aqui ficaram um tanto aquém do desejado. Modelos mais sofisticados e o agrupamento das frases de forma que o tradutor tivesse mais contexto seriam formas de melhorar o resultado, mas não tive tempo hábil para implementar.

[TTS] Foi a parte mais trabalhosa do projeto. Foram feitos experimentos com modelos bastante simples como o `pyttsx3`, mas a qualidade do audio era extremamente robótica. Depois foram feitos experimentos com modelos mais sofisticados como o `bark` e o `coqui`, mas a falta de GPU nâo permitiu que os experimentos fossem feitos a contento. O modelo `microsoft/speecht5_tts` foi um bom compromisso de meio de caminho e permitiria futuramente treinar vozes próprias.


### _en_

This project uses a series of machine learning models to, from a video in Portuguese, create a new version of the same video, but with a (still somewhat rudimentary) voice over in English.

This project was created using `Python Poetry`. To run the project, after cloning it from Github, simply access the project directory and run in your terminal:
```bash
poetry install
poetry env use
```

Next, you need to organize the data a little. To run the project correctly it is necessary to place a `.mp4` file in the `data/raw` folder. IT IS **IMPORTANT** that the file is named `case_ai.mp4`.

Once this is done, just run the `main.py` file.

Care was taken to use _open source_ machine learning models in most phases of the project. Some of these models deserve some consideration.

[TRANSCRIPTION] `openai-whisper` In addition to providing good quality, the model delivers several useful outputs in its results, such as files that can be used directly to create subtitles as well as very efficient drafting.

[TRANSLATION] The results here were somewhat less than desired. More sophisticated models and grouping sentences so that the translator has more context would be ways to improve the result, but I didn't have the time to implement them.

[TTS] It was the most laborious part of the project. Experiments were carried out with very simple models like `pyttsx3`, but the audio quality was extremely robotic. Later, experiments were carried out with more sophisticated models such as `bark` and `coqui`, but the lack of GPU did not allow the experiments to be carried out satisfactorily. The `microsoft/speecht5_tts` model was a good compromise and would allow us to train our own voices in the future.