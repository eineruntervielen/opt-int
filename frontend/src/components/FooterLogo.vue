<template>
  <a class="transition hover:-translate-y-3 hover:cursor-pointer duration-300"
     :href="href">
    <img class="w-10"
         :src="imgUrl(filename)"
         :alt="alt">
  </a>
</template>

<script>
import LogoGitHub from "../assets/img/LogoGithub.png";
import LogoDiscord from "../assets/img/LogoDiscord.svg";

export default {
  name: "FooterLogo",
  props: {
    alt: String,
    href: String,
    filename: String
  },
  methods: {
    imgUrl(filename) {
      switch (filename) {
        case "LogoGitHub":
          return LogoGitHub
        case "LogoDiscord":
          return LogoDiscord
      }
    }
  }
};
</script>