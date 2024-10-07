# Body40


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **int** | ID of the Folder or File to add the Custom Tag to | 
**document_custom_tag** | [**CustomTag**](CustomTag.md) |  | 

## Example

```python
from procore_sdk.models.body40 import Body40

# TODO update the JSON string below
json = "{}"
# create an instance of Body40 from a JSON string
body40_instance = Body40.from_json(json)
# print the JSON string representation of the object
print(Body40.to_json())

# convert the object into a dict
body40_dict = body40_instance.to_dict()
# create an instance of Body40 from a dict
body40_from_dict = Body40.from_dict(body40_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


