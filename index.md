---
title: Home
description: "Research homepage for Asif Khan, focusing on machine learning and AI for medicine."
---

<section class="hero">
  <div class="hero__portrait">
    <img class="hero__photo" src="{{ site.profile.photo | relative_url }}" alt="Portrait of {{ site.profile.name }}" width="208" height="260">
    <div class="hero__links" aria-label="Profile links">
      <a href="https://scholar.google.com/citations?user=Akp4gEwAAAAJ&amp;hl=en" target="_blank" rel="noopener">Google Scholar</a>
      <a href="https://github.com/MdAsifKhan" target="_blank" rel="noopener">GitHub</a>
      <a href="https://x.com/KhanAsif__" target="_blank" rel="noopener">X</a>
    </div>
    <div class="hero__links hero__links--contact" aria-label="CV and email">
      <a href="{{ '/assets/pdf/AsifKhanCV.pdf' | relative_url }}" target="_blank" rel="noopener">CV</a>
      <a href="mailto:{{ site.email }}">Email</a>
    </div>
    <address class="hero__address">210 Longwood Avenue, Boston, MA 02115</address>
  </div>
  <div class="hero__content">
    <div class="hero__heading">
      <h1>{{ site.profile.name }}</h1>
      <p class="hero__tagline">{{ site.profile.tagline }}</p>
    </div>
    <p class="hero__lead">
      I am a Staff Scientist at <a href="{{ site.profile.organization_url }}" target="_blank" rel="noopener">Harvard Medical School</a>, working with <a href="https://www.sanderlab.org/#/people/chrissander" target="_blank" rel="noopener">Chris Sander</a> and <a href="https://www.deboramarkslab.com/debora-marks" target="_blank" rel="noopener">Debbie Marks</a>.
    </p>
    <p>
      My research focuses on representation learning and generative models for large-scale patient health data and cancer biology. My goal is to develop AI methods that use such data for cancer early detection and prognosis, helping clinicians make informed decisions and improve care pathways.
    </p>
    <p>
      I develop models that learn from longitudinal health records to track changes in patient health and estimate risk across cancer types. I focus on making these models scalable, robust, and well-calibrated across patient populations and clinical settings. I also use drug and CRISPR perturbation data to model cellular responses and guide combination therapy design.
    </p>
    <p class="hero__affiliations">
      I am also a visiting postdoc with <a href="https://isbscience.org/people/jennifer-hadlock-md/" target="_blank" rel="noopener">Jenn Hadlock</a> at <a href="{{ site.affiliations[1].url }}" target="_blank" rel="noopener">ISB</a> and a research associate with <a href="https://researchers.mgh.harvard.edu/profile/14398376/Erica-Warner" target="_blank" rel="noopener">Erica Warner</a> at <a href="{{ site.affiliations[2].url }}" target="_blank" rel="noopener">MGH’s early detection clinic</a>, with affiliations at the <a href="{{ site.affiliations[3].url }}" target="_blank" rel="noopener">Ludwig Center at Harvard</a> and <a href="https://www.broadinstitute.org/" target="_blank" rel="noopener">Broad Institute</a>.
    </p>
    <p>
      I completed my PhD in Machine Learning at the University of Edinburgh with <a href="https://homepages.inf.ed.ac.uk/amos/" target="_blank" rel="noopener">Amos Storkey</a>, working on geometry for deep representation learning. I continue to study geometric methods for representation learning and interpreting large language models.
    </p>
  </div>
</section>

<section class="section selected-work">
  <header class="section__header">
    <h2>Selected Publications</h2>
    <a class="section__more" href="{{ '/publications/' | relative_url }}">All publications ↗</a>
  </header>
  <div class="paper-list">
    {% for paper in site.selected_work %}
      <article class="paper-row">
        <div class="paper-row__content">
          <div class="paper-row__meta">{{ paper.venue }} <span>{{ paper.year }}</span></div>
          <h3><a href="{{ paper.url }}" target="_blank" rel="noopener">{{ paper.title }}</a></h3>
          <ul class="paper-row__tags" aria-label="Research topics">
            {% for tag in paper.tags %}
              <li>#{{ tag }}</li>
            {% endfor %}
          </ul>
          <div class="paper-row__visuals">
            {% if paper.preview %}
              <a class="paper-preview" href="{{ paper.url }}" target="_blank" rel="noopener" aria-label="Read {{ paper.title | escape }}">
                <img src="{{ paper.preview.path | relative_url }}" alt="{{ paper.preview.alt | escape }}" width="{{ paper.preview.width }}" height="{{ paper.preview.height }}" loading="lazy" decoding="async">
              </a>
            {% endif %}
            <div class="paper-row__figure">
              <img src="{{ paper.figure.path | relative_url }}" alt="{{ paper.figure.alt | escape }}" width="{{ paper.figure.width }}" height="{{ paper.figure.height }}" loading="lazy" decoding="async">
            </div>
          </div>
        </div>
        <a class="paper-row__arrow" href="{{ paper.url }}" target="_blank" rel="noopener" aria-label="Read {{ paper.title }}">↗</a>
      </article>
    {% endfor %}
  </div>
</section>
