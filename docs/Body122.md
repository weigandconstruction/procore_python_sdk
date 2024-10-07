# Body122


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**bim_viewpoints** | [**List[Body121BimViewpointOneOf2]**](Body121BimViewpointOneOf2.md) | An array of BIM Viewpoint payloads. Limited to 100 items per request | 

## Example

```python
from procore_sdk.models.body122 import Body122

# TODO update the JSON string below
json = "{}"
# create an instance of Body122 from a JSON string
body122_instance = Body122.from_json(json)
# print the JSON string representation of the object
print(Body122.to_json())

# convert the object into a dict
body122_dict = body122_instance.to_dict()
# create an instance of Body122 from a dict
body122_from_dict = Body122.from_dict(body122_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


