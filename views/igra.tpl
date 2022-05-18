% import model

%rebase('base.tpl')
 
  <h2>{{igra.pravilni_del_gesla()}}</h2>

  Nepravilni ugibi: <b>{{igra.nepravilni_ugibi()}}</b> <br>

  <img src="/img/{{igra.stevilo_napak()}}.jpg" alt="obesanje">

  % if stanje == model.ZMAGA:

  <h1>ZMAGA!</h1>
  <form action="/igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>

  % elif stanje == model.PORAZ:

  <h1>PORAZ!</h1>
  Pravilno geslo: <b>{{igra.geslo}}</b>
    <form action="/igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>

  % else:
  <form action="/igra/{{id_igre}}/" method="post">
    Črka: <input type='text' name='crka'>
    <button type="submit">Ugibaj</button>
  </form>

  % end