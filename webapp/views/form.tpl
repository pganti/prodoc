<html>
  <head>
      <title>POC Doc Generation</title>
  </head>
  <body>
    <form method="post" action="/genpdf">
        <fieldset>
            <legend>POC Data Input</legend>
            <ul>
                <li>Domain Name (no www): <input name='domain'>
                </li>
                <li>Customer Label: <input name='cust'>
                </li>
            </ul><input type='submit' value='Submit Form'>
        </fieldset>
    </form>
    
    <p>{{message}}</p>

  </body>
</html>
