# Body73


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | Company ID | 
**line_item_type** | [**LineItemType2**](LineItemType2.md) |  | 

## Example

```python
from procore_sdk.models.body73 import Body73

# TODO update the JSON string below
json = "{}"
# create an instance of Body73 from a JSON string
body73_instance = Body73.from_json(json)
# print the JSON string representation of the object
print(Body73.to_json())

# convert the object into a dict
body73_dict = body73_instance.to_dict()
# create an instance of Body73 from a dict
body73_from_dict = Body73.from_dict(body73_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


