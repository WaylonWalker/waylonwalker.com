<li class='post {{post['templateKey']}}'>
<a href="/{{post['slug']}}/">
    <h2 class='title'>{{post['title']}}</h2>
    <p class='description'>{{post['long_description']}}</p>
    <div>
        <p class='date'>{{post['date'].year}}-{{post['date'].month}}-{{post['date'].day}}</p>
        <p>
        {{post['templateKey']}}
        </p>
    </div>
</a>
</li>
