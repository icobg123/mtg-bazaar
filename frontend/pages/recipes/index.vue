<template>
  <v-main>
    <v-container class="container--fluid">
      <v-row justify="center" align="center">
        <v-col cols="12" sm="12" md="12">

          <div class="d-flex flex-column justify-content-between">
            <h3 class="mb-3">La Recipes</h3>
            <v-btn color="red" to="/recipes/add" class="mr-auto mb-3 ">Add Recipe</v-btn>
          </div>
          <v-row justify="center" align="center">

            <template v-for="recipe in recipes">
              <v-col cols="12" sm="6" md="4" lg="3" :key="recipe.id" class="mb-4">
                <recipe-card :onDelete="deleteRecipe" :recipe="recipe"></recipe-card>
              </v-col>
            </template>
          </v-row>
        </v-col>
      </v-row>
    </v-container>

  </v-main>
</template>

<script>

import RecipeCard from "~/components/RecipeCard.vue";


const sampleData = [
  {
    id: 1,
    name: "Jollof Rice",
    picture: "/images/food-1.jpeg",
    ingredients: "Beef, Tomato, Spinach",
    difficulty: "easy",
    prep_time: 15,
    prep_guide:
      "Lorem ipsum dolor sit amet consectetur adipisicing elit. Omnis, porro. Dignissimos ducimus ratione totam fugit officiis blanditiis exercitationem, nisi vero architecto quibusdam impedit, earum "
  },
  {
    id: 2,
    name: "Macaroni",
    picture: "/images/food-2.jpeg",
    ingredients: "Beef, Tomato, Spinach",
    difficulty: "easy",
    prep_time: 15,
    prep_guide:
      "Lorem ipsum dolor sit amet consectetur adipisicing elit. Omnis, porro. Dignissimos ducimus ratione totam fugit officiis blanditiis exercitationem, nisi vero architecto quibusdam impedit, earum "
  },
  {
    id: 3,
    name: "Fried Rice",
    picture: "/images/banner.jpg",
    ingredients: "Beef, Tomato, Spinach",
    difficulty: "easy",
    prep_time: 15,
    prep_guide:
      "Lorem ipsum dolor sit amet consectetur adipisicing elit. Omnis, porro. Dignissimos ducimus ratione totam fugit officiis blanditiis exercitationem, nisi vero architecto quibusdam impedit, earum "
  }
];

export default {
  head() {
    return {
      title: "Recipes list"
    };
  },
  components: {
    RecipeCard
  },
  async asyncData({$axios, params}) {
    try {
      let recipes = await $axios.$get(`/api/recipes/`);
      return {recipes};
    } catch (e) {
      return {recipes: []};
    }
  },
  data() {
    return {
      recipes: []
    };
  },
  methods: {
    async deleteRecipe(recipe_id) {
      try {
        await this.$axios.$delete(`/api/recipes/${recipe_id}/`); // delete recipe
        let newRecipes = await this.$axios.$get("/api/recipes/"); // get new list of recipes
        this.recipes = newRecipes; // update list of recipes
        // return newRecipes;
      } catch (e) {
        console.log(e);
      }
    }
  },
  // middleware: 'auth',

}
</script>

<style scoped>

</style>
