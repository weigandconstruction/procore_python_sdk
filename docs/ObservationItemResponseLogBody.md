# ObservationItemResponseLogBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | The ID of the Project the Observation Item Response Log belongs to | 
**response_log** | [**ResponseLog**](ResponseLog.md) |  | 
**status** | **str** | The Status of the Observation | [optional] 

## Example

```python
from procore_sdk.models.observation_item_response_log_body import ObservationItemResponseLogBody

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationItemResponseLogBody from a JSON string
observation_item_response_log_body_instance = ObservationItemResponseLogBody.from_json(json)
# print the JSON string representation of the object
print(ObservationItemResponseLogBody.to_json())

# convert the object into a dict
observation_item_response_log_body_dict = observation_item_response_log_body_instance.to_dict()
# create an instance of ObservationItemResponseLogBody from a dict
observation_item_response_log_body_from_dict = ObservationItemResponseLogBody.from_dict(observation_item_response_log_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


