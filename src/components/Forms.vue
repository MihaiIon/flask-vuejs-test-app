<template>
  <div class="c-forms">
    <!-- <app-toast :data="toastData" /> -->
    <create-author-form @toast="handleToast" />
    <v-divider class="c-forms__divider" dark />
    <create-note-form @toast="handleToast" />
  </div>
</template>

<script>
import AppToast from "@/components/AppToast.vue";
import FormCard from "@/components/FormCard.vue";
import CreateAuthorForm from "@/components/CreateAuthorForm.vue";
import CreateNoteForm from "@/components/CreateNoteForm.vue";

export default {
  name: "Forms",
  components: {
    AppToast,
    CreateAuthorForm,
    CreateNoteForm,
    FormCard,
  },
  data() {
    return {
      toastData: null,
    };
  },
  methods: {
    handleToast(data) {
      this.toastData = data;
    },
  },
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
