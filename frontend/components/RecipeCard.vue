<template>

  <v-card
    class="mx-auto"
    max-width="400"
  >
    <v-img
      class="white--text align-end"
      height="200px"
      :src="recipe.picture"
    >

      <v-card-title>{{ recipe.name }}</v-card-title>
    </v-img>

    <v-card-subtitle class="pb-0">
      Number 10
    </v-card-subtitle>

    <v-card-text class="text--primary">
      <strong>Ingredients:</strong>
      {{ recipe.ingredients }}


    </v-card-text>

    <v-card-actions class="d-flex flex-column align-center">
      <v-btn
        :to="`/recipes/${recipe.id}/`"
        color="orange"
        text
      >
        View
      </v-btn>

      <v-btn
        class="m-0"
        :to="`/recipes/${recipe.id}/edit/`"
        color="orange"
        text
      >
        Edit
      </v-btn>

      <v-btn
        class="m-0"
        @click="onDelete(recipe.id)"
        color="orange"
        text
      >
        Delete
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "RecipeCard",
  props: ["recipe", "onDelete"]
}
</script>

<style scoped>

</style>
