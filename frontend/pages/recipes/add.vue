<template>
  <v-main class="">
    <v-container>
      <v-row class="row">
        <v-col cols="12" class="text-center my-3">
          <h2 class="mb-3 display-4 text-uppercase">{{ recipe.name }}</h2>
        </v-col>
        <v-col md="6" class="col-md-6 mb-4">
          <img
            v-if="preview"
            class="img-fluid"
            style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
            :src="preview"
            alt
          >
          <img
            v-else
            class="img-fluid"
            style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
            src="@/static/images/placeholder.jpg"
          >
        </v-col>
        <v-col md="4" class="col-md-4">
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
    </v-container>
  </v-main>
</template>

<script>
export default {
  head() {
    return {
      title: "Add Recipe"
    };
  },
  data() {
    return {
      difficulty: ['Easy', 'Medium', 'Hard'],
      recipe: {
        name: "BAd RQ",
        picture: "",
        ingredients: "1 Bad Reuqest",
        difficulty: "Hard",
        prep_time: 60,
        prep_guide: "KLorum Impsum"
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
      const config = {
        headers: {"content-type": "multipart/form-data"}
      };
      let formData = new FormData();
      for (let data in this.recipe) {
        formData.append(data, this.recipe[data]);
      }
      // debugger
      try {
        let response = await this.$axios.$post("/api/recipes/", formData, config);
        this.$router.push("/recipes/");
      } catch (e) {
        console.log(e.response);
      }
    }
  }
};
</script>

<style scoped>

</style>
