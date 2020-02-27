Autor: Szymon Żak                   27.02.2020, Kraków

Spis treści:
1. Opis programu
2. Zastosowane biblioteki
3. Uruchomienie
4. Serwer
5. Klient
6. Dodatkowe informacje
-------------------------------------
1. Opis programu

    Program realizuje funkcję czatu internetowego.
    Zawiera się w dwóch plikach, odpowiednio jeden dla serwera 
    a drugi dla klienta.
    Przeznaczony jest dla Pythona 3.

2. Zastosowane biblioteki
    
    W programie wykorzystano biblioteki standardowe Pythona.
    Dla serwera:
    - socket (do obsługi komunikacji poprzez gniazdka sieciowe)
    - threading (do obsługi wielu klientów naraz)
    
    Dla klienta:
    - socket (do obsługi komunikacji)
    - threading (do jednoczesnej obsługi GUI i komunikacji sieciowej)
    - tkinter (do stworzenia GUI)

3. Uruchomienie

    W celu uruchomienia programu przygotowano następujące skrypty, zarówno
    dla platformy Windows (pliki z rozszerzeniem .bat) jak i Linux (pliki shellowe)
    W celu uruchomienia serwera należy wykonać odpowiedni skrypt:
    - dla Windowsa - polecenie "start_server"
    - dla Linuxa - polecenie "./start_server.sh"
    Analogicznie, aby uruchomić klienta należy wpisać:
    - dla Windowsa - "start_client"
    - dla Linuxa - "./start_client.sh"
    
    Każdy program należy uruchamiać w oddzielnym oknie konsoli.
    
    Alternatywnie, gdyby powyższy sposób nie zadziałał, można uruchomić
    każdy z programów wchodząc po prostu do folderów
    src/client i src/serwer i uruchamiając programy komendami 
    "python3 server.py" i "python3 client.py". 
    
    Aby program odpowiednio zadziałał należy posiadać zainstalowanego Pythona
    w wersji 3 i dało się go wywołać poleceniem "python3". 
    Musi mieć też zainstalowaną bibliotekę tkinter (jednak zasadniczo 
    jest ona zazwyczaj dodawana do standardowej instalacji Pythona).
    Program przetestowano na platformie wyposażonej zarówno w Pythona 3.7
    jak i 3.8 i w obydwu przypadkach zadziałał prawidłowo.
    Uwaga!
    Tkinkter zmienił nazwę pakietu w Pythonie 3.7 na tkinter. Dzięki poniższemu kodowi
    
    "try:
        from tkinter import *
    except:
        from Tkinter import *"
    
    program powinien zadziałać na każdej wersji Pythona 3.
    
    Warto też pamiętać że przed uruchomieniem klienta należy uruchomić serwer.
    W przeciwnym wypadku program nie będzie mógł nawiązać połączenia z serwerem i wyłączy się.
    
4. Serwer

    Pliki serwera znajdują się w katalogu 'src/server'.
    Serwer domyślnie działa na porcie 33000. 
    Można go zmienić w pliku źródłowym "server.py" (zmienna PORT).
    Serwer nasłuchuje i poprzez gniazdka może się połączyć z klientami.
    Kiedy nadchodzi połączenie, serwer tworzy oddzielny wątek do obsługi klienta.
    Po zakończeniu połączenia z danym klientem następuje zakończenie pętli wykonywania wątku.
    Aby zatrzymać działanie serwera należy wyłączyć okno terminala z aktywnym procesem.

5. Klient

    Pliki klienta znajdują się w katalogu 'src/client'.
    Na początku, przy uruchomieniu klienta ukazuje się okno z dwoma polami.
    Górne pole jest przeznaczone do wpisania adresu (domyślnie 'localhost'),
    natomiast dolne pole jest przeznaczone do wpisania portu (domyślnie 33000).
    Następnie należy nacisnąć przycisk "Ustaw", 
    a jeśli dane zostały wypełnione poprawnie, pojawi się okno czatu.
    Na początku należy wypełnić dolne pole, swoją nazwą i nacisnąć klawisz "enter"
    lub przycisk "wyślij".
    Następnie czat jest już gotowy do użycia. Wystarczy wpisać wiadomość
    i nacisnać "enter" lub "wyślij".
    Ważne: aby klient zadziałał, początkowo musi zostać uruchomiony serwer.
    W przeciwnym wypadku  wystąpi 
    "ConnectionRefusedError: [WinError 10061] Nie można nawiązać połączenia,
    ponieważ komputer docelowy aktywnie go odmawia".
    Aby zamknąć klienta, należy użyć przycisku 'X' w prawym górnym rogu aplikacji.
    
6. Dodatkowe informacje

    Dany program może działać po sieci i być uruchamiany na różnych komputerach.
    Wtedy, należy zmienić adres serwera z 'localhost' na adres komputera na którym
    jest uruchomiony serwer.
   
7. Bibliografia
 
    Dokumentacja tkinter:
    https://docs.python.org/3/library/tk.html
    
    Dokumentacja threading:
    https://docs.python.org/3/library/threading.html
    
    Dokumentacja socket:
    https://docs.python.org/3/library/socket.html
    
    Użyta wersja Pythona przy pisaniu projektu: 3.7