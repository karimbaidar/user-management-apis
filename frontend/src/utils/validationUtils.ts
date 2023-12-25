import { computed } from "vue";

export const hasInvalidChars = computed(() => {
  return (inputField: string) => {
    try {
      return /[0-9!@#$%^&*()_+{}|:<>?~]/.test(inputField);
    } catch (error) {
      console.error(error);
      return true;
    }
  };
});

export const hasEmptyFields = (user: any) => {
  return computed(() => {
    return Object.values(user.value).some((value: any) => value === "");
  });
};

export const isButtonDisabled = (
  isSubmitting: any,
  errors: any,
  hasEmptyFields: any
) => {
  return computed(() => {
    return (
      isSubmitting.value ||
      Object.values(errors).some((error: any) => error) ||
      errors["create_user"]  !== null ||
      hasEmptyFields.value
    );
  });
};

export const showInvalidInputMessage = (hasInvalidChars: any, errors: any) => {
  return computed(() => {
    return (inputField: string, fieldName: string) => {
      const hasError = hasInvalidChars.value(inputField);

      if (hasError) {
        errors[fieldName] = true;
      } else {
        errors[fieldName] = false; // Reset error state
      }

      return hasError;
    };
  });
};

export const serverResponseMessage = (errors: any) => {
  return computed(() => {
    if (errors["create_user"]) {
      const errorMessages = Object.values(errors["create_user"].response.data).flat();
      return errorMessages.join(", ");
    } else {
      return null;
    }
  });
};
