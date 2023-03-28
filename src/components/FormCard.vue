<template>
  <v-card class="c-form-card" elevation="0" :disabled="saving" dark>
    <slot></slot>
  </v-card>
</template>

<script>
export default {
  name: "FormCard",
  props: {
    saving: {
      type: Boolean,
      default: false,
    }
  }
};
</script>

<style scoped lang="scss">
$form-card-padding: 25px;

.c-form-card {
  width: 500px;
  padding: $form-card-padding;
}
</style>
