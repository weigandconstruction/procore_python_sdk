# Body107


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**deletes** | [**List[Body107DeletesInner]**](Body107DeletesInner.md) | An array of objects containing resource id to delete | 

## Example

```python
from procore_sdk.models.body107 import Body107

# TODO update the JSON string below
json = "{}"
# create an instance of Body107 from a JSON string
body107_instance = Body107.from_json(json)
# print the JSON string representation of the object
print(Body107.to_json())

# convert the object into a dict
body107_dict = body107_instance.to_dict()
# create an instance of Body107 from a dict
body107_from_dict = Body107.from_dict(body107_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


