---
title: Home
description: "Research homepage for Asif Khan, focusing on machine learning and AI for medicine."
---

<section class="hero">
  <div class="hero__portrait">
    <img class="hero__photo" src="{{ site.profile.photo | relative_url }}" alt="Portrait of {{ site.profile.name }}">
  </div>
  <div class="hero__content">
    <p class="eyebrow">Machine Learning &amp; AI for Medicine</p>
    <h1>{{ site.profile.name }}</h1>
    <p class="hero__role">{{ site.profile.tagline }}</p>
    <p class="hero__lead">
      I am a Staff Scientist at Harvard Medical School, where I work with <a href="https://www.sanderlab.org/#/people/chrissander" target="_blank" rel="noopener">Chris Sander</a> and <a href="https://www.deboramarkslab.com/debora-marks" target="_blank" rel="noopener">Debbie Marks</a> on machine learning and AI methods for cancer research and clinical applications.
    </p>
    <p>
      My research interests include representation learning and generative models for large-scale data. My current work develops scalable models for longitudinal electronic health records that are robust and well-calibrated for pan-cancer risk stratification. I also work with drug and CRISPR perturbation data to model cellular responses and guide the design of combination therapies.
    </p>
    <p>
      Before joining Harvard, I completed my PhD in Machine Learning at the University of Edinburgh under the supervision of <a href="https://homepages.inf.ed.ac.uk/amos/" target="_blank" rel="noopener">Amos Storkey</a>. My doctoral research focused on geometry for deep representation learning. I continue to develop geometric methods for understanding representation learning and interpreting large language models.
    </p>
    <div class="hero__links" aria-label="Primary links">
      <a href="{{ '/publications/' | relative_url }}">Publications</a>
      <a href="{{ '/assets/pdf/AsifKhanCV.pdf' | relative_url }}" target="_blank" rel="noopener">CV</a>
      <a href="mailto:{{ site.email }}">Email</a>
      <a href="https://x.com/KhanAsif__" target="_blank" rel="noopener">X</a>
    </div>
  </div>
</section>

<section class="section selected-work">
  <header class="section__header">
    <p class="eyebrow">Selected work</p>
    <h2>Recent publications</h2>
  </header>
  <div class="paper-list">
    {% for paper in site.selected_work %}
      <article class="paper-row">
        <div class="paper-row__meta">{{ paper.venue }} <span>{{ paper.year }}</span></div>
        <div class="paper-row__content">
          <h3><a href="{{ paper.url }}" target="_blank" rel="noopener">{{ paper.title }}</a></h3>
          <p>{{ paper.detail }}</p>
        </div>
        <a class="paper-row__arrow" href="{{ paper.url }}" target="_blank" rel="noopener" aria-label="Read {{ paper.title }}">↗</a>
      </article>
    {% endfor %}
  </div>
  <p class="section__more"><a href="{{ '/publications/' | relative_url }}">View all publications →</a></p>
</section>

<section class="section research-directions">
  <header class="section__header">
    <p class="eyebrow">Research</p>
    <h2>Current directions</h2>
  </header>
  <div class="direction-list">
    {% for direction in site.research_directions %}
      <article class="direction">
        <span class="direction__number">0{{ forloop.index }}</span>
        <div>
          <h3>{{ direction.title }}</h3>
          <p>{{ direction.detail }}</p>
        </div>
      </article>
    {% endfor %}
  </div>
</section>

<section class="section background">
  <header class="section__header">
    <p class="eyebrow">Background</p>
    <h2>Education</h2>
  </header>
  <div class="background__items">
    {% for item in site.education %}
      <div class="background__item">
        <p><strong>{{ item.degree }}</strong></p>
        <p>{{ item.years | replace: '--', '–' }}</p>
        <p>{{ item.detail }}</p>
      </div>
    {% endfor %}
  </div>
</section>
