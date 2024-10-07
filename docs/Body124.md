# Body124


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**bim_view_folder** | [**Body124BimViewFolder**](Body124BimViewFolder.md) |  | 

## Example

```python
from procore_sdk.models.body124 import Body124

# TODO update the JSON string below
json = "{}"
# create an instance of Body124 from a JSON string
body124_instance = Body124.from_json(json)
# print the JSON string representation of the object
print(Body124.to_json())

# convert the object into a dict
body124_dict = body124_instance.to_dict()
# create an instance of Body124 from a dict
body124_from_dict = Body124.from_dict(body124_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


