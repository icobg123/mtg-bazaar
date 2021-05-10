<template>
  <v-main class="container my-5">
    <v-row class="row">
      <v-col class="col-12 text-center my-3">
        <h2 class="mb-3 display-4 text-uppercase">{{ recipe.name }}</h2>
      </v-col>
      <v-col class="col-md-6 mb-4">
        <img v-if="!preview" class="img-fluid"
             style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);" :src="recipe.picture">
        <img v-else class="img-fluid" style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
             :src="preview">
      </v-col>
      <v-col class="col-md-4">
        <v-form @submit.prevent="submitRecipe">
          <!--            <div class="form-group">-->
          <!--              <label for>Recipe Name</label>-->
          <v-text-field label="Recipe Name" type="text" v-model="recipe.name"></v-text-field>
          <!--            </div>-->
          <!--            <div class="form-group">-->
          <!--              <label for>Ingredients</label>-->
          <v-text-field label="Ingredients" v-model="recipe.ingredients" type="text"
          ></v-text-field>
          <!--            </div>-->
          <!--            <div class="form-group">-->
          <!--              <label for>Food picture</label>-->
          <!--                        <input type="file" name="file" @change="onFileChange">-->

          <v-file-input accept="image/*" label="Food picture" type="file" name="file"
                        @change="onFileChange"></v-file-input>
          <!--            <v-file-input accept="image/*" label="Food picture" type="file" name="file" @change="onFileChange"></v-file-input>-->
          <!--            </div>-->
          <!--            <v-row class="row flex-column">-->
          <!--              <v-col md="12" class="col-md-6">-->
          <!--                <div class="form-group">-->
          <!--                  <label for>Difficulty</label>-->
          <v-select :items="difficulty" label="Difficulty" outlined v-model="recipe.difficulty"
                    class="pa-0 ma-0"></v-select>
          <!--                </div>-->
          <!--              </v-col>-->
          <!--              <v-col md="12" class="col-md-6">-->
          <!--                <div class="form-group">-->
          <!--                  <label for>-->
          <!--                    Prep time-->
          <!--                    <small></small>-->
          <!--                  </label>-->
          <v-text-field label="Prep time (minutes)" type="number" v-model="recipe.prep_time"
          ></v-text-field>
          <!--                </div>-->
          <!--              </v-col>-->
          <!--            </v-row>-->
          <!--            <div class="form-group mb-3">-->
          <!--              <label for>Preparation guide</label>-->
          <v-textarea solo label="Preparation guide" v-model="recipe.prep_guide"
                      rows="8"></v-textarea>
          <!--            </div>-->
          <v-btn type="submit" class="btn btn-primary">Submit</v-btn>
        </v-form>
      </v-col>
    </v-row>
  </v-main>
</template>
<script>
export default {
  head() {
    return {
      title: "Edit Recipe"
    }
  },
  async asyncData({$axios, params}) {
    try {
      let recipe = await $axios.$get(`/api/recipes/${params.id}/`);
      console.log(recipe);
      return {recipe};
    } catch (e) {
      return {recipe: []};
    }
  },
  data() {
    return {
      difficulty: ['Easy', 'Medium', 'Hard'],

      recipe: {
        name: "",
        picture: "",
        ingredients: "",
        difficulty: 'Hard',
        prep_time: 60,
        prep_guide: ""
      },
      preview: ""
    };
  },
  methods: {
    onFileChange(e) {
      console.log(e);
      let files = e;
      // let files = e.target.files || e.dataTransfer.files;
      if (files == null) {
        // if (!files.length) {
        return;
      }
      this.recipe.picture = files;
      // this.recipe.picture = files[0];
      this.createImage(files);
      // this.createImage(files[0]);
    },
    createImage(file) {
      // let image = new Image();
      let reader = new FileReader();
      let vm = this;
      reader.onload = e => {
        console.log(e);
        vm.preview = e.target.result;
      };
      // debugger
      reader.readAsDataURL(file);
    },
    async submitRecipe() {
      let editedRecipe = this.recipe
      if (typeof editedRecipe.image === 'string' && editedRecipe.picture.indexOf("http://") !== -1) {
        delete editedRecipe["picture"]
      }
      const config = {
        headers: {"content-type": "multipart/form-data", 'Access-Control-Allow-Origin': '*',}
      };
      let formData = new FormData();
      for (let data in editedRecipe) {
        formData.append(data, editedRecipe[data]);
      }
      try {
        let response = await this.$axios.$patch(`/api/recipes/${editedRecipe.id}/`, formData, config);
        this.$router.push("/recipes/");
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>

<style>
</style>
