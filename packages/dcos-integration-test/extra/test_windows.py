import logging

import requests

import test_helpers

__maintainer__ = 'kensipe'
__contact__ = 'orchestration-team@mesosphere.io'

log = logging.getLogger(__name__)


def deploy_test_app_and_check_windows(dcos_api_session, app: dict, test_uuid: str):
    """This method deploys the python test server container and then checks
    if the container is up and can accept connections.
    """
    # Increase the timeout of the application to avoid failing while pulling the docker image
    with dcos_api_session.marathon.deploy_and_cleanup(app, timeout=2400, ignore_failed_tasks=True):
        service_points = dcos_api_session.marathon.get_app_service_endpoints(app['id'])
        r = requests.get('http://{}:{}'.format(service_points[0].host, service_points[0].port))
        if r.status_code != 200:
            msg = "Test server replied with non-200 reply: '{0} {1}. "
            msg += "Detailed explanation of the problem: {2}"
            raise Exception(msg.format(r.status_code, r.reason, r.text))


def test_if_docker_app_can_be_deployed_windows(dcos_api_session):
    """Marathon app inside docker deployment integration test.

    Verifies that a marathon app inside of a docker daemon container can be
    deployed and accessed as expected on Windows.
    """
    deploy_test_app_and_check_windows(dcos_api_session, *test_helpers.marathon_test_app_windows())
