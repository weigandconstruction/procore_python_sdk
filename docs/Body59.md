# Body59


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**bim_view_folder** | [**Body59BimViewFolder**](Body59BimViewFolder.md) |  | 

## Example

```python
from procore_sdk.models.body59 import Body59

# TODO update the JSON string below
json = "{}"
# create an instance of Body59 from a JSON string
body59_instance = Body59.from_json(json)
# print the JSON string representation of the object
print(Body59.to_json())

# convert the object into a dict
body59_dict = body59_instance.to_dict()
# create an instance of Body59 from a dict
body59_from_dict = Body59.from_dict(body59_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


