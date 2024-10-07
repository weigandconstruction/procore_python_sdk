# Checklist5DefaultResponsePhrasing

Conforming/Deficient responses used for items having the default response type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conforming_response** | **str** | Conforming response of the default response set | [optional] 
**deficient_response** | **str** | Deficient/Non-conforming response of the default response set | [optional] 
**var_global** | **bool** | Boolean flag indicating if the default response phrasing is Procore-provided | [optional] 

## Example

```python
from procore_sdk.models.checklist5_default_response_phrasing import Checklist5DefaultResponsePhrasing

# TODO update the JSON string below
json = "{}"
# create an instance of Checklist5DefaultResponsePhrasing from a JSON string
checklist5_default_response_phrasing_instance = Checklist5DefaultResponsePhrasing.from_json(json)
# print the JSON string representation of the object
print(Checklist5DefaultResponsePhrasing.to_json())

# convert the object into a dict
checklist5_default_response_phrasing_dict = checklist5_default_response_phrasing_instance.to_dict()
# create an instance of Checklist5DefaultResponsePhrasing from a dict
checklist5_default_response_phrasing_from_dict = Checklist5DefaultResponsePhrasing.from_dict(checklist5_default_response_phrasing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


