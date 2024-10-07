# Body60


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**view** | **str** | Specify response schema view | [optional] 
**bim_view_folders** | [**List[Body59BimViewFolder]**](Body59BimViewFolder.md) | An array of nested BIM View Folder payload | 

## Example

```python
from procore_sdk.models.body60 import Body60

# TODO update the JSON string below
json = "{}"
# create an instance of Body60 from a JSON string
body60_instance = Body60.from_json(json)
# print the JSON string representation of the object
print(Body60.to_json())

# convert the object into a dict
body60_dict = body60_instance.to_dict()
# create an instance of Body60 from a dict
body60_from_dict = Body60.from_dict(body60_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


