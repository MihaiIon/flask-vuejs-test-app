<template>
  <div id="app" class="c-app" data-app>
    <note-list class="c-app__note-list" />
    <forms class="c-app__forms" />
  </div>
</template>

<script>
import Forms from '@/components/Forms.vue'
import NoteList from '@/components/NoteList.vue'

export default {
  name: 'app',
  components: {
    Forms,
    NoteList
  }
}
</script>

<style lang="scss">
$text-field-label-top: 8px !default;
$note-list-width: 300px;

html, body, #app {
  height: 100vh;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

.c-app {
  position: relative;
}

.c-app__note-list {
  position: absolute;
  left: 0px;
  top: 0px;
  bottom: 0px;
  z-index: 1;

  width: $note-list-width;
}

.c-app__forms {
  position: absolute;
  left: $note-list-width;
  top: 0px;
  bottom: 0px;
  right: 0px;
  z-index: 1;

  background-color: #333;
}
</style>
