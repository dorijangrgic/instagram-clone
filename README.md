# instagram-clone

Aplikacija sadrži administratora čiji su korisničko ime i lozinka "admin".
Administracijsko sučelje nalazi se na adresi "http://127.0.0.1:5100/admin/".
REST API url-ovi nalaze se na adresi "http://127.0.0.1:5100/api/", a prilikom testiranja korišten je REST klijent Insomnia.
Pomoću REST APIja moguće je registrirai korisnika pogađanjem endpointa "users/registration/".
Također login je na endpointu "login/". Prilikom login-a korisnik dobije vlastiti token s kojim pristupa zaštićenim resursima dodajući u zaglavlje zahtjeva "Authorization: Token <token>".
Stvaranje novih poruka moguće je pogađanjem endpointa "create_post/" no s obzirom na nemogućnost unosa slike prilikom testiranja (Insomnia),
poruke se mogu isključivo stvoriti koriteći admin sučelje.
Registrirani korisnici mogu zapratiti i otpratiti druge korisnike na endpointu "follow/id_korisnika".
Javni timeline dostupan je svim korisnicima (registriranim i neregistriranim) na endpointu "public", dok je privatni timeline dostupan na endpointu "private".
Privatni timeline sadrži poruke svih korisnika koje trenutni korisnik prati dok javni timeline sadrži sve poruke svih korisnika.
