{%- assign m = include.page.date | date: "%-m" -%}
{%- case m -%}
{%- when '1' -%}OCAK
{%- when '2' -%}ŞUBAT
{%- when '3' -%}MART
{%- when '4' -%}NİSAN
{%- when '5' -%}MAYIS
{%- when '6' -%}HAZİRAN
{%- when '7' -%}TEMMUZ
{%- when '8' -%}AĞUSTOS
{%- when '9' -%}EYLÜL
{%- when '10' -%}EKİM
{%- when '11' -%}KASIM
{%- when '12' -%}ARALIK
{%- endcase -%}
{{- include.page.date | date: " %Y" -}}
