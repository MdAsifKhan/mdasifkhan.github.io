---
title: Academic Activities
permalink: /activities/
description: "Talks, teaching, academic service, funding, and mentoring by Asif Khan."
---

<section class="page-intro">
  <h1>Academic activities</h1>
</section>

<div class="activities-list">
  <article class="activities-card">
    <h2>Talks &amp; seminars</h2>
    <ul class="talk-list">
      <li>
        <span class="talk-list__year">2026</span>
        <span><strong>Pan-cancer risk assessment with an EHR foundation model that predicts what happens next and when.</strong> Selected talk, <a href="https://newenglandcompbio.org/" target="_blank" rel="noopener">New England Computational Biology Symposium (NECB)</a>, Microsoft Research New England.</span>
      </li>
      <li>
        <span class="talk-list__year">2026</span>
        <span><strong>Pan-cancer risk stratification via a foundation model of patient health histories.</strong> Flash talk, The Cancer Prevention Research Conference, Atlanta.</span>
      </li>
      <li>
        <span class="talk-list__year">2026</span>
        <span><strong>Pan-cancer risk assessment for early detection and prevention from real-world longitudinal clinical records.</strong> Cancer Early Detection and Diagnostics Clinic, Massachusetts General Hospital.</span>
      </li>
      <li>
        <span class="talk-list__year">2026</span>
        <span><strong>Tutorial on AI in Oncology.</strong> AI in Cancer Research Symposium, Ludwig Center at Harvard.</span>
      </li>
      <li>
        <span class="talk-list__year">2025</span>
        <span><strong>Cancer risk prediction from large-scale electronic health records.</strong> Hadlock Lab Seminar, Institute for Systems Biology.</span>
      </li>
      <li>
        <span class="talk-list__year">2025</span>
        <span><strong>Representation learning on longitudinal health trajectories using LLMs for disease risk assessment.</strong> MIT-MGB AI Cures, Cambridge.</span>
      </li>
    </ul>
  </article>

  <article class="activities-card">
    <h2>Teaching</h2>
    <ul>
      <li>Tutor &amp; marker for Probabilistic Modelling and Reasoning (2019–2020), University of Edinburgh.</li>
      <li>Marker for Machine Learning Practical (2019–2021), Introductory Applied Machine Learning (2019–2021), and Data Mining &amp; Exploration (2020–2021), University of Edinburgh.</li>
      <li>Teaching assistant for <a href="https://github.com/SmartDataAnalytics/Knowledge-Graph-Analysis-Programming-Exercises" target="_blank" rel="noopener">Knowledge Graph Analysis</a> (WS17/18, WS18/19), University of Bonn, delivering tutorial, course content preparation, exercise and exam assessment.</li>
    </ul>
  </article>

  <article class="activities-card">
    <h2>Student mentoring</h2>
    <ul>
      {% for student in site.students %}
        <li><strong>{{ student.name }}</strong> ({{ student.years }}) — {{ student.program }}.</li>
      {% endfor %}
    </ul>
  </article>

  <article class="activities-card">
    <h2>Reviewing</h2>
    <ul>
      <li>Journal reviewer: Journal of Machine Learning Research (JMLR).</li>
      <li>NeurIPS 2026 (Top Reviewer); ICML 2026 (Technical Reviewer: Gold).</li>
      <li>NeurIPS 2025, ICML 2025 (Outstanding Reviewer), NeurIPS 2024 (Top Reviewer), ICML 2024 (Best Reviewer), NeurIPS 2023 (Top Reviewer), ICML 2023.</li>
      <li>AISTATS 2022–2023 (Top Reviewer), NeurIPS 2022 (Top Reviewer), ICLR 2022 (Highlighted Reviewer).</li>
      <li>Workshops: CAO and GRaM @ ICLR 2026, TS4Health @ NeurIPS 2025, ML4LMS @ ICML 2024, SynS &amp; ML @ ICML 2023, ML4PS @ NeurIPS 2021/2022/2023.</li>
    </ul>
  </article>

  <article class="activities-card">
    <h2>Funding &amp; awards</h2>
    <ul>
      <li>Best Poster Award, The Early Detection of Cancer Conference, 2026.</li>
      <li>Best Poster Award, The Cancer Prevention Research Conference, 2026.</li>
      <li><a href="https://www.the-ici-fund.org/recipients/details/multi-risk-cancer-prediction-using-deep-sequential-modeling-of-large-scale-longitudinal-ehrs" target="_blank" rel="noopener">Innovation in Cancer Informatics (2025-2027).</a></li>
      <li><a href="https://www.daad.de/en/the-daad/postdocnet/fellows/fellows/#Khan-Asif" target="_blank" rel="noopener">AI for Science Fellow, DAAD Postdoc-NeT-AI program 2024.</a></li>
      <li>NeurIPS Scholar Award 2022.</li>
      <li>PhD Scholarship (2019-2023).</li>
    </ul>
  </article>

</div>
