CAN_NOT_FIND_CONFIG_FILE = "Cannot find config file under user directory, try 'watcard --config'."
CONFIG_FILE_HAS_BEEN_ENCRYPTED = "Config file has been encrypted, needs to be decrypted first. Try 'watcard -d'."
ADDING_FUND_SUCCESSFULLY = "Adding ${} to account '{}' successfully."
ADDING_FUND_FAILED = "Adding ${} to account '{}' failed."
WILL_ENCRYPT_YOUR_CONFIG_FILE_WARNING = "This will encrypt your config file! Do you want to proceed?"
IS_ALREADY_ENCRYPTED = "Your config file is already encrypted. To decrypt it, please try 'watcard -d'."
CONFIG_FILE_SUCCESSFULLY_ENCRYPTED = "Config file successfully encrypted."
WILL_DECRYPT_YOUR_CONFIG_FILE_WARNING = "This will decrypt your config file! Do you want to proceed?"
IS_ALREADY_DECRYPTED = "Your config file is already decrypted. To encrypt it, please use 'watcard -e'."
CONFIG_FILE_SUCCESSFULLY_DECRYPTED = "Config file successfully decrypted."
WILL_RESET_YOUR_CONFIG_FILE_WARNING = "This will reset your config file! Do you want to proceed?"
CONFIG_FILE_ALREADY_EXISTS = "Config file '.watcard_config' already exists."
OPENING_CONFIG_FILE = "Opening {}."
GENERATE_CONFIG_FILE_SUCCESSFULLY = "Generate config file at user directory successfully. Please fill your information."
RESET_CONFIG_FILE_SUCCESSFULLY = "Reset config file successfully. Try 'watcard --config' to fill your information."
DECRYPTING_CONFIG_FILE_FAILED = "Decrypting config file failed."
INVALID_PASSWORD = "Invalid password."
INVALID_CONFIG_FILE = "Invalid config file. Try 'watcard --valid' to check if your config file is valid."
VALID_CONFIG_FILE = (
    "The config file is valid. If you're still getting an error, try doing 'watcard -r' to reset your " "config file."
)
USERNAME_ERROR = "userName has special characters, please remove them."
ORDNAME_ERROR = "ordName has characters other than letters, please remove them."
PHONENUMBER_ERROR = "phoneNumber isn't formatted correctly, please check it."
POSTALCODE_ERROR = "ordPostalCode is not a valid postal code, please check it."
ORDCITY_ERROR = "ordCity has characters other than letters, please remove them."
EMAIL_ERROR = "ordEmailAddress is not a valid email address, please check it."
PAYMETHOD_ERROR = "paymentMethod is not CC, please check it."
CARDOWNER_ERROR = "trnCardOwner has characters other than letters, please remove them."
CARDTYPE_ERROR = "trnCardType is an unsupported card type, please check it."
CARDNUMBER_ERROR = "trnCardNumber is not a valid card number, please check it."
EXPMONTH_ERROR = "trnExpMonth is not valid, please check it."
EXPYEAR_ERROR = "trnExpYear is not valid, please check it."
CVD_ERROR = "trnCardCvd is not valid, please check it."
