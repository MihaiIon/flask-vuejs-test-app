<template>
  <div class="c-note-list">
    <v-list class="c-note-list__list" flat dark>
      <v-subheader>All Notes</v-subheader>
      <v-list-item-group v-model="selectedNote">
        <template v-for="(note, index) in formattedNotes">
          <v-list-item :key="note.title + note.content">
            <v-list-item-content>
              <v-list-item-title
                class="c-note-list__item-title"
                v-text="note.title"
              />
              <v-list-item-subtitle
                class="c-note-list__item-content"
                v-text="note.content"
              />
              <v-list-item-subtitle
                class="c-note-list__item-author"
                v-text="note.authorFullName"
              />
            </v-list-item-content>
          </v-list-item>
          <v-divider v-if="index < notes.length - 1" :key="index"></v-divider>
        </template>
      </v-list-item-group>
    </v-list>
  </div>
</template>

<script>
import $backend from "../backend";

export default {
  name: "NoteList",
  data() {
    return {
      selectedNote: null,
      notes: [],
    };
  },
  async created() {
    await this.fetchNotes();
  },
  computed: {
    formattedNotes() {
      return this.notes.map((note) => {
        return {
          title: note["title"],
          content: note["content"],
          authorFullName: note["author_full_name"],
        };
      });
    },
  },
  methods: {
    async fetchNotes() {
      try {
        const { data: notes } = await $backend.fetchNotes();
        console.info(notes);
        this.notes = notes;
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>

<style lang="scss">
.c-note-list__list {
  height: 100%;
}

.c-note-list__item-author {
  font-size: 10px;
  color: #129077 !important;

  &:before {
    content: "- ";
  }
}
</style>
