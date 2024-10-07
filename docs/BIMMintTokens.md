# BIMMintTokens


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | Bim mint tokens for the project. | [optional] 

## Example

```python
from procore_sdk.models.bim_mint_tokens import BIMMintTokens

# TODO update the JSON string below
json = "{}"
# create an instance of BIMMintTokens from a JSON string
bim_mint_tokens_instance = BIMMintTokens.from_json(json)
# print the JSON string representation of the object
print(BIMMintTokens.to_json())

# convert the object into a dict
bim_mint_tokens_dict = bim_mint_tokens_instance.to_dict()
# create an instance of BIMMintTokens from a dict
bim_mint_tokens_from_dict = BIMMintTokens.from_dict(bim_mint_tokens_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


