# CustomTag

Document Custom Tag object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Custom Tag | 

## Example

```python
from procore_sdk.models.custom_tag import CustomTag

# TODO update the JSON string below
json = "{}"
# create an instance of CustomTag from a JSON string
custom_tag_instance = CustomTag.from_json(json)
# print the JSON string representation of the object
print(CustomTag.to_json())

# convert the object into a dict
custom_tag_dict = custom_tag_instance.to_dict()
# create an instance of CustomTag from a dict
custom_tag_from_dict = CustomTag.from_dict(custom_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


