% import model

%rebase('base.tpl')
 
  <h2>{{igra.pravilni_del_gesla()}}</h2>

  Nepravilni ugibi: <b>{{igra.nepravilni_ugibi()}}</b> <br>

  <img src="/img/{{igra.stevilo_napak()}}.jpg" alt="obesanje">

  % if stanje == model.ZMAGA:

  <h1>ZMAGA!</h1>
  <form action="/nova_igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>

  % elif stanje == model.PORAZ:

  <h1>PORAZ!</h1>
  Pravilno geslo: <b>{{igra.geslo}}</b>
    <form action="/nova_igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>

  % else:

  <form action="/igra/" method="post">
    Črka: <input type='text' name='crka'>
    <button type="submit">Ugibaj</button>
  </form>

  <form action="/igra/" method="post">
  <table>
    % for vrstica in ["ERTZUIOPŠ", "ASDFGHJKLČŽ", "CVBNM"]:
      <tr><td>
      % for crka in vrstica:
        % barva = "prazno" if crka not in igra.crke else ("prav" if crka in igra.geslo else "narobe")
        <input type="submit" name="crka" value="{{crka}}" class="{{barva}}">
      % end
      </td></tr>
    % end
  </table>
  </form>

  % end