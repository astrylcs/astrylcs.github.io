---
layout: post
class: post-template
---
{%- assign zodiac = "
♈&emsp;Koç Burcu ve Yükselen Koçlar,
♉&emsp;a,
♊&emsp;b,
♋&emsp;c,
♌&emsp;d,
♍&emsp;e,
♎&emsp;f,
♏&emsp;g,
♐&emsp;h,
♑&emsp;i,
♒&emsp;j,
♓&emsp;k,
⛎&emsp;l
" | split: "," -%}
<div id="select">
{%- for i in zodiac -%}
<article class="post-card no-image">
<div class="post-card-content">
<a class="post-card-content-link" href="#">
<header class="post-card-header">
<h2 class="post-card-title">
{{ i }}
</h2>
</header>
</a>
</div>
</article>
{%- endfor -%}
</div>
<script>
</script>
