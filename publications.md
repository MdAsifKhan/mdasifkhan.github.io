---
title: Publications
permalink: /publications/
description: "Peer-reviewed work and preprints by Asif Khan."
---

<section class="page-intro">
  <h1>Publications</h1>
  <p><a href="https://scholar.google.com/citations?user=Akp4gEwAAAAJ&hl=en" target="_blank" rel="noopener">Google Scholar ↗</a></p>
  <nav class="publication-nav" aria-label="Publication categories">
    <a href="#conferences">Conferences</a>
    <a href="#journals">Journals</a>
    <a href="#preprints">Preprints</a>
    <a href="#workshops">Workshops</a>
    <a href="#thesis">Thesis</a>
  </nav>
</section>

<section class="publication-group" id="conferences" aria-labelledby="conferences-heading">
  <h2 class="publication-group__heading" id="conferences-heading">Conferences</h2>
  <div class="publication-list">
    {% bibliography -f papers -q @*[category=conference] %}
  </div>
</section>

<section class="publication-group" id="journals" aria-labelledby="journals-heading">
  <h2 class="publication-group__heading" id="journals-heading">Journals</h2>
  <div class="publication-list">
    {% bibliography -f papers -q @*[category=journal] %}
  </div>
</section>

<section class="publication-group" id="preprints" aria-labelledby="preprints-heading">
  <h2 class="publication-group__heading" id="preprints-heading">Preprints</h2>
  <div class="publication-list">
    {% bibliography -f papers -q @*[category=preprint] %}
  </div>
</section>

<section class="publication-group" id="workshops" aria-labelledby="workshops-heading">
  <h2 class="publication-group__heading" id="workshops-heading">Workshops</h2>
  <div class="publication-list">
    {% bibliography -f papers -q @*[category=workshop] %}
  </div>
</section>

<section class="publication-group" id="thesis" aria-labelledby="thesis-heading">
  <h2 class="publication-group__heading" id="thesis-heading">Thesis</h2>
  <div class="publication-list">
    {% bibliography -f papers -q @*[category=thesis] %}
  </div>
</section>
