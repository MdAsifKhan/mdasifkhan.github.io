---
title: Contact
permalink: /contact/
description: "Get in touch with Asif Khan."
---

<section class="page-intro">
  <h1>Contact</h1>
  <p>
    I enjoy collaborations where machine learning meets biology and clinical practice. Reach out if you would like to talk about research.
  </p>
</section>

<div class="contact-card">
  <div class="contact-card__items">
    <a class="contact-icon" href="mailto:{{ site.email }}" aria-label="Email {{ site.profile.name }}">✉︎</a>
    <div class="contact-card__details">
      {% if site.contact.office %}
        <span>{{ site.contact.office }}</span>
      {% endif %}
      {% if site.contact.address_lines %}
        <address>{{ site.contact.address_lines | join: '<br>' }}</address>
      {% endif %}
      {% if site.contact.phone %}
        <span>{{ site.contact.phone }}</span>
      {% endif %}
    </div>
  </div>
  {% assign form_action = site.contact.form_action | default: '' | strip %}
  <form class="contact-form" method="POST"{% if form_action != '' %} action="{{ form_action }}"{% endif %}>
    {% if site.contact.form_subject %}
      <input type="hidden" name="_subject" value="{{ site.contact.form_subject }}">
    {% endif %}
    <input type="hidden" name="_template" value="box">
    <input type="hidden" name="_captcha" value="false">
    <div class="contact-form__group">
      <label for="name">Name</label>
      <input id="name" name="name" type="text" autocomplete="name" required>
    </div>
    <div class="contact-form__group">
      <label for="email">Email</label>
      <input id="email" name="email" type="email" autocomplete="email" required>
    </div>
    <div class="contact-form__group">
      <label for="message">Message</label>
      <textarea id="message" name="message" rows="5" required></textarea>
    </div>
    <div class="contact-form__group contact-form__group--actions">
      <button type="submit" class="button">Send Message</button>
    </div>
  </form>
  <p class="contact-card__hint">
    Messages are delivered to <a href="mailto:{{ site.email }}">{{ site.email }}</a> via FormSubmit. The first submission will trigger a confirmation email from FormSubmit to enable the form.
  </p>
</div>
