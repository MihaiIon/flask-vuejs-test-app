<template>
  <form-card :saving="saving">
    <v-form class="c-create-author-form" @submit.prevent="submitForm">
      <v-text-field
        v-model="authorFirstName"
        label="Author First Name"
        outlined
        solo
        required
      ></v-text-field>
      <v-text-field
        v-model="authorLastName"
        label="Author Last Name"
        outlined
        solo
        required
      ></v-text-field>
      <v-btn @click="resetForm" color="secondary">Reset</v-btn>
      <v-btn
        class="c-create-author-form__submit-btn"
        type="submit"
        color="primary"
        >Save</v-btn
      >
    </v-form>
  </form-card>
</template>

<script>
import FormCard from "@/components/FormCard.vue";
import $backend from "../backend";

export default {
  name: "CreateAuthorForm",
  components: { FormCard },
  data() {
    return {
      authorFirstName: "",
      authorLastName: "",
      saving: false,
    };
  },
  methods: {
    async submitForm() {
      try {
        this.saving = true;
        const data = {
          'first_name': this.authorFirstName,
          'last_name': this.authorLastName,
        };
        const response = await $backend.createAuthor(data);
        console.info(response);
        this.resetForm();
      } catch (error) {
        console.error(error);
      } finally {
        this.saving = false;
      }
    },
    resetForm() {
      this.authorFirstName = "";
      this.authorLastName = "";
    },
  },
};
</script>

<style lang="scss">
.c-create-author-form__submit-btn {
  margin-left: 10px;
  background-color: #129077 !important;
}
</style>
