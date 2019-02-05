{% for post in site.posts %}
  <article class="post-card {{ page.class }} {% unless post.image %}no-image{% endunless %}">
    {% if post.image %}
    <a class="post-card-image-link" href="{{ post.url }}">
      <div class="post-card-image" style="background-image: url({{ post.image }})"></div>
    </a>
    {% endif %}
    <div class="post-card-content">
      <a class="post-card-content-link" href="{{ post.url }}">
        <header class="post-card-header">
          {% if post.date %}
          <span class="post-card-tags">{{ post.tag }}</span>
          {% endif %}
          <h2 class="post-card-title">{{ post.title }}</h2>
        </header>
      </a>
    </div>
  </article>
{% endfor %}