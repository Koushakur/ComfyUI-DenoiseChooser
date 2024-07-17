
class DenoiseChooser:
   @classmethod
   def INPUT_TYPES(cls):
      data_in = {
         "required": {
            "Latent": ("LATENT",),
            "FloatIfEmpty": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 100.0, "step": 0.05}),
            "FloatIfNot": ("FLOAT", {"default": 0.75, "min": 0.0, "max": 100.0, "step": 0.05})
         }
      }
      return data_in

   CATEGORY = "advanced"
   FUNCTION = "func"
   RETURN_TYPES = ("LATENT", "FLOAT")

   def func(self, Latent, FloatIfEmpty, FloatIfNot):
      tNonZeroes = Latent['samples'].count_nonzero().item()

      if tNonZeroes > 0:
         return (Latent, FloatIfNot if FloatIfNot <= 1.0 else FloatIfNot/100)
      else:
         return (Latent, FloatIfEmpty if FloatIfEmpty <= 1.0 else FloatIfEmpty/100)
