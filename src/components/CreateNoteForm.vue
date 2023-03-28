<template>
  <form-card :saving="saving">
    <v-form class="c-create-note-form" @submit.prevent="submitForm">
      <v-text-field
        v-model="noteTitle"
        label="Note title"
        outlined
        solo
        required
      ></v-text-field>
      <v-textarea
        v-model="noteContent"
        label="Note content"
        :rows="3"
        outlined
        solo
        required
      ></v-textarea>
      <v-select
        v-model="selectedAuthorFullName"
        label="Select an Author"
        :items="authorsFullName"
        :loading="loadingAuthors"
        :menu-props="{ maxHeight: '200px' }"
        @click="fetchAuthors"
        outlined
        solo
        required
      ></v-select>
      <v-btn @click="resetForm" color="secondary">Reset</v-btn>
      <v-btn
        class="c-create-note-form__submit-btn"
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
  name: "CreateNoteForm",
  components: { FormCard },
  data() {
    return {
      noteTitle: "",
      noteContent: "",
      authors: [],
      authorsFullName: [],
      selectedAuthorFullName: null,
      loadingAuthors: false,
      saving: false,
    };
  },
  computed: {
    selectedAuthorId() {
      if (!this.selectedAuthorFullName) return null;

      const selectedAuthor = this.authors.filter(
        (author) => author["full_name"] == this.selectedAuthorFullName
      )[0];
      return selectedAuthor ? selectedAuthor["id"] : null;
    },
  },
  methods: {
    async fetchAuthors() {
      this.loadingAuthors = true;
      try {
        const { data: authors } = await $backend.fetchAuthors();
        this.authors = authors;
        this.authorsFullName = authors.map((author) => author["full_name"]);
        console.info(this.authors);
        console.info(this.authorsFullName);
      } catch (error) {
        console.error(error);
      } finally {
        this.loadingAuthors = false;
      }
    },
    async submitForm() {
      try {
        this.saving = true;
        const data = {
          title: this.noteTitle,
          content: this.noteContent,
          author_id: this.selectedAuthorId,
        };
        const response = await $backend.createNote(data);
        console.info(response);
        this.resetForm();
      } catch (error) {
        console.error(error);
      } finally {
        this.saving = false;
      }
    },
    resetForm() {
      this.noteTitle = "";
      this.noteContent = "";
      this.selectedAuthorFullName = null;
    },
  },
};
</script>

<style lang="scss">
.c-create-note-form__submit-btn {
  margin-left: 10px;
  background-color: #129077 !important;
}
</style>
