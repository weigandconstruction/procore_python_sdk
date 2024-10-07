# Body27


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**updates** | [**List[PurchaseOrderContract1]**](PurchaseOrderContract1.md) | Updated Purchase Order Contracts | 

## Example

```python
from procore_sdk.models.body27 import Body27

# TODO update the JSON string below
json = "{}"
# create an instance of Body27 from a JSON string
body27_instance = Body27.from_json(json)
# print the JSON string representation of the object
print(Body27.to_json())

# convert the object into a dict
body27_dict = body27_instance.to_dict()
# create an instance of Body27 from a dict
body27_from_dict = Body27.from_dict(body27_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


