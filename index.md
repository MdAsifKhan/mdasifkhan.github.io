---
title: Home
description: "Research homepage for Asif Khan, focusing on machine learning for precision oncology."
---

<section class="hero">
  <div class="hero__intro">
    <div class="hero__header">
      <img class="hero__photo" src="{{ site.profile.photo | relative_url }}" alt="Portrait of Asif Khan">
      <div class="hero__heading">
        <h1 class="hero__title">Asif Khan</h1>
        <span class="hero__eyebrow">Machine Learning &amp; AI for Medicine</span>
        <span class="hero__role">Postdoctoral Fellow · Harvard Medical School</span>
      </div>
    </div>
    <p class="hero__lead">
      I am a Postdoctoral Fellow at Harvard Medical School, working with <a href="https://www.sanderlab.org/#/people/chrissander" target="_blank" rel="noopener">Chris Sander</a>. Before Harvard, I completed my PhD with <a href="https://homepages.inf.ed.ac.uk/amos/" target="_blank" rel="noopener">Amos Storkey</a> in the <a href="https://www.bayeswatch.com" target="_blank" rel="noopener">Bayesian and Neural Systems Group</a> at the University of Edinburgh. My doctoral thesis was on the geometry for deep representation learning.
    </p>
    <p class="hero__lead hero__lead--secondary">
    My current research lies at the intersection of machine learning and biomedicine, addressing two critical challenges in cancer biology: early detection using longitudinal patient records and optimization of combination therapies through mechanistic models of drug response. Late-stage diagnosis remains the primary cause of cancer mortality, as many patients present when curative treatment is no longer possible. By training AI on large-scale clinical data, our work aims to identify high-risk individuals who can benefit from earlier intervention and effective treatment strategies. My work is centered around following topics:
    </p>
    <ul class="hero__summary-list">
      <li><strong>Representation learning from longitudinal EHRs</strong>: Developing foundation models that encode patient histories into continuous representation spaces of patient health states for downstream survival and risk assessments.</li>
      <li><strong>Uncertainty-aware cancer risk prediction</strong>: Building well-calibrated, robust, and generalizable models that capture distribution shifts across hospitals and populations.</li>
      <li><strong>AI-guided therapy design</strong>: Learning differential equation models that capture molecular dynamics under drug perturbations to inform combination therapies.</li>
    </ul>
    <div class="hero__details">
      <div class="hero__block">
        <h2 class="hero__block-title">Interests</h2>
        <ul class="hero__highlights">
          {% for item in site.interests %}
            <li>{{ item }}</li>
          {% endfor %}
        </ul>
      </div>
      <div class="hero__block">
        <h2 class="hero__block-title">Education</h2>
        <ul class="hero__timeline">
          <li>
            <strong>PhD in Machine Learning, University of Edinburgh</strong><span>2018–2023</span>
            <div class="hero__timeline-detail">Bayesian and Neural Systems Group (Prof. Amos Storkey)</div>
          </li>
          <li>
            <strong>MSc in Computer Science, University of Bonn</strong><span>2016–2018</span>
            <div class="hero__timeline-detail">Focus on machine learning and knowledge graphs</div>
          </li>
        </ul>
      </div>
    </div>
    <div class="button-row">
      <a class="button" href="{{ '/publications/' | relative_url }}">View Publications</a>
      <a class="button button--ghost" href="mailto:{{ site.email }}">Email Me</a>
    </div>
    <div class="hero__social">
      <span class="hero__social-label">Connect</span>
      <div class="social-links">
        {% for link in site.social_links %}
          <a href="{{ link.url }}" aria-label="{{ link.label }}" target="_blank" rel="noopener">
            {% include social-icon.html icon=link.icon label=link.label %}
          </a>
        {% endfor %}
      </div>
    </div>
  </div>
</section>

<section class="section research">
  <h2 class="section__title">Research Overview</h2>
  <div class="research__pillars">
    <div class="focus-list">
      {% for highlight in site.research_highlights %}
        <article class="focus-card research-feature">
          <h3>{{ highlight.title }}</h3>
          <div class="research-feature__body">
            {% if highlight.image %}
              <div class="research-feature__media">
                <img src="{{ highlight.image | relative_url }}" alt="{{ highlight.image_alt }}">
              </div>
            {% endif %}
            <p class="research-feature__text">
              {{ highlight.detail }}
            </p>
          </div>
        </article>
      {% endfor %}
    </div>
