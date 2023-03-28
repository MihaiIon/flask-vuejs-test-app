<template>
  <div class="c-forms">
    <create-author-form />
    <v-divider class="c-forms__divider" dark />
    <create-note-form />
  </div>
</template>

<script>
import FormCard from "@/components/FormCard.vue";
import CreateAuthorForm from "@/components/CreateAuthorForm.vue";
import CreateNoteForm from "@/components/CreateNoteForm.vue";

export default {
  name: "Forms",
  components: { CreateAuthorForm, CreateNoteForm, FormCard },
};
</script>

<style>
.c-forms {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.c-forms__divider {
  width: 250px;
  margin: 25px 0;
}
</style>
