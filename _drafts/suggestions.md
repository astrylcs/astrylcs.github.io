{% unless page.nosuggestions %}
            <aside class="read-next outer">
                <div class="inner">
                    <div class="read-next-feed">
                        {% if page.date %}
                            <article class="read-next-card" style="background-image: url(/cover.jpg)">
                                <header class="read-next-card-header">
                                    <small class="read-next-card-header-sitetitle">&mdash; {{ site.title }} &mdash;</small>
                                    <h3 class="read-next-card-header-title"><a>{% include tag.html page=page %}</a></h3>
                                </header>
                                <div class="read-next-divider">
                                    <svg viewBox="0 0 24 24">
                                        <path d="M13 14.5s2 3 5 3 5.5-2.463 5.5-5.5S21 6.5 18 6.5c-5 0-7 11-12 11C2.962 17.5.5 15.037.5 12S3 6.5 6 6.5s4.5 3.5 4.5 3.5"/>
                                    </svg>
                                </div>
                                <div class="read-next-card-content">
                                    <ul>
                                        {% for post in site.posts %}
                                            {% capture post_tag %}{% include tag.html page=post %}{% endcapture %}
                                            {% capture page_tag %}{% include tag.html page=page %}{% endcapture %}
                                            {% if post_tag == page_tag %}
                                                <li><a href="{{ post.url }}">{{ post.title }}</a></li>
                                            {% endif %}
                                        {% endfor %}
                                    </ul>
                                </div>
                            </article>
                        {% endif %}
                        {% if page.next %}
                            <article class="post-card {{ page.next.class }} {% unless page.next.image %}no-image{% endunless %}">
                                {% if page.next.image %}
                                    <a class="post-card-image-link" href="{{ page.next.url }}">
                                        <div class="post-card-image" style="background-image: url({% include image.html page=page.next %})"></div>
                                    </a>
                                {% endif %}
                                <div class="post-card-content">
                                    <a class="post-card-content-link" href="{{ page.next.url }}">
                                        <header class="post-card-header">
                                            {% if page.next.date %}
                                                <span class="post-card-tags">{% include tag.html page=page.next %}</span>
                                            {% endif %}
                                            <h2 class="post-card-title">{{ page.next.title }}</h2>
                                        </header>
                                    </a>
                                </div>
                            </article>
                        {% endif %}
                        {% if page.previous %}
                            <article class="post-card {{ page.previous.class }} {% unless page.previous.image %}no-image{% endunless %}">
                                {% if page.previous.image %}
                                    <a class="post-card-image-link" href="{{ page.previous.url }}">
                                        <div class="post-card-image" style="background-image: url({% include image.html page=page.previous %})"></div>
                                    </a>
                                {% endif %}
                                <div class="post-card-content">
                                    <a class="post-card-content-link" href="{{ page.previous.url }}">
                                        <header class="post-card-header">
                                            {% if page.previous.date %}
                                                <span class="post-card-tags">{% include tag.html page=page.previous %}</span>
                                            {% endif %}
                                            <h2 class="post-card-title">{{ page.previous.title }}</h2>
                                        </header>
                                    </a>
                                </div>
                            </article>
                        {% endif %}
                    </div>
                </div>
            </aside>
{% endunless %}
