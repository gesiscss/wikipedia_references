# wikipedia_references

[![Binder](https://notebooks.gesis.org/binder/badge_logo.svg)](https://notebooks.gesis.org/binder/v2/gh/gesiscss/wikipedia_references/master)


The dataset consists of json files where article_id is used as file name.

Each file is represented as list of “References”. Each references is a dictionary with the following keys:
* "first_rev_id" type: Integer, first revision where the reference was inserted (the same value is represented in “ins” as the first element of the list and in "rev_id" of the first element in the "change_sequence")
* "first_hash_id" type: String, hash value of the first version of token_id (WikiWho) list of the reference (the same value is represented as "hash_id" of the first element in the "change_sequence")
* "first_editor_id"  type: String, user_id or IP address of the first revision where the reference was inserted (the same value is represented as "editor_id" of the first element in the "change_sequence" 
* "deleted" type: Boolean, indicator if the reference exists in the last available revision
* "ins" type: List of Integers, list of revisions where reference was inserted (includes the first revision mentioned as "first_rev_id")
* "ins_editor" type: List of Strings, list of user_id or IP addresses of editors where reference was inserted (includes the first user mentioned as "first_editor_id")
* "del" type: List of Integers, list of revisions where reference was deleted from the article or reference was modified in a way that less than 25% of tokens remained, 
* "del_editor“ type: List of Strings, list of user_id or IP addresses of editors where reference was deleted or reference was modified in a way that less than 25% of tokens remained 
* "modif" type: List of Integers, list of revisions where reference was modified, or reinserted with modification
* "change_sequence" type: List of Dictionaries, with information about tokens, editors and revisions where reference was modified (the first element represent the first revision where reference was inserted), where:
  * "hash_id" type: String, hash value of the token_id (WikiWho) list of the reference version
  * "rev_id" type: Integer, revision number of the particular version of the reference
  * "editor_id" type: String, user_id or IP address of the revision editor
  * "tokens" type: List of Strings, ordered list of tokens (created by WikiWho) that represents the particular version of the reference (the list has the same length as "token_editors")
  * "token_editors" type: List of Strings, ordered list of user_ids or IP addresses of editors that were first who added the corresponding token (see "tokens") to Wikipedia article 
