<template>
  <StandardLayout>
    <nav></nav>
    <router-view />
  </StandardLayout>
</template>

<script>
import StandardLayout from "@/layouts/StandardLayout.vue";

export default {
  components: {
    StandardLayout,
  },
};
</script>
